/**
* @NApiVersion 2.x
* @NScriptType Suitelet
* @NModuleScope Public
*/

/* 

------------------------------------------------------------------------------------------
Script Information
------------------------------------------------------------------------------------------

Name:
SQL Query Tool

ID:
_sql_query_tool

Description
A utility for running SQL queries against a NetSuite instance.


------------------------------------------------------------------------------------------
Developer(s)
------------------------------------------------------------------------------------------

Tim Dietrich
• timdietrich@me.com
• https://timdietrich.me


------------------------------------------------------------------------------------------
History
------------------------------------------------------------------------------------------

20200801 - Tim Dietrich
• Initial version.

20200805 - Tim Dietrich
• Added support for displaying the results in a sublist.

20200806 - Tim Dietrich
• Adjusted the embedded jQuery to resolve conflicts.

20201027 - Tim Dietrich
• Added support for saving / loading scripts to / from the File Cabinet.
• Added support for exporting query results.
• Changed how the query execution time is calculated.
• Longer record text values (> 300 characters) are now truncated before being 
	displayed in the results sublist.
• If the JSON-encoded recordset is > 100000 characters, then only the 
	first record is displayed.

*/


var 
	file,	
	log,
	query,
	serverWidget,
	sqlFolderName = 'SuiteQL Queries',
	sqlFolderID,
	sqlFiles;


define( [ 'N/file', 'N/log', 'N/query', 'N/ui/serverWidget' ], main );


function main( fileModule, logModule, queryModule, serverWidgetModule ) {

	// Set module references.
	file = fileModule;
	log = logModule;
	query= queryModule;
	serverWidget = serverWidgetModule;
	
	// Get the ID of the SuiteQL Scripts folder.
	sqlFolderID = sqlFolderGet();
	
	// Get the files in the SuiteQL Scripts folder.
	sqlFiles = sqlFolderFilesGet();			
	
    return {
    
    	onRequest: function( context ) {

			// Create a form.
			var form = serverWidget.createForm(
				{
					title: 'SuiteQL Query Tool',
					hideNavBar: false
				}
			);		
			
			// Add a hidden "action" field.
			actionFieldAdd( form );												
												
			// If the form has been submitted...
			if ( context.request.method == 'POST' ) {	

				switch ( context.request.parameters.custpage_field_action ) {
				
					case 'export-results':
						exportQueryResults( context, form );
						break;
				
					case 'load-step-1':
						loadQueryFormPrep( context, form );
						break;
						
					case 'load-step-2':
						loadQueryProcess( context, form );
						break;						
	
					case 'run-query':
						queryRun( context, form );	
						break;		
						
					case 'save-step-1':
						saveQueryFormPrep( context, form );
						break;
						
					case 'save-step-2':
						saveQueryProcess( context, form );
						break;	
						
					default:
						form.addSubmitButton( { label: 'Run Query' } );	
						loadQueryButtonAdd( form );	
						queryFieldAdd( context, form );										

				}					
			
			} else {
			
				// Add a "Run Query" submit button.
				form.addSubmitButton( { label: 'Run Query' } );			
			
				// Add a "Load Query" button.
				loadQueryButtonAdd( form );		
				
				// Add the query field.
				queryFieldAdd( context, form );								
			
			}
			
			// Add client-side Javascript to the form.
			javascriptAdd( context, form );				
				
			// Display the form.
			context.response.writePage( form );			
	
        }
        
    }

}


function actionFieldAdd( form ) {

	// Add the action field.
	// This is used to determine what action to take when the form is submitted.
	var actionField = form.addField(
		{
			id: 'custpage_field_action',
			type: serverWidget.FieldType.TEXT,
			label: 'Action'
		}								
	);	
	
	// Hide the action field.
	actionField.updateDisplayType(
		{
			displayType: serverWidget.FieldDisplayType.HIDDEN
		}
	);	
	
	// Set the default value for the action field.
	actionField.defaultValue = 'run-query';	
			
}


function exportResultsButtonAdd( form ) {

	// Client-side script that will be run when the Export button is clicked.
	var exportFunction =
		'document.getElementById(\'custpage_field_action\').value = (\'export-results\');'
		+ 'document.main_form.submit();';			
	
	// Add an "Export Results" button.	
	form.addButton( 
		{
			id: 'custpage_button_add',
			label: 'Export Results',
			functionName: exportFunction
		} 
	);	
			
}


function exportQueryResults ( context, form ) {

	// Run the query.
	var queryResults = query.runSuiteQL(
		{
			query: context.request.parameters.custpage_field_query
		}
	); 					

	// Get the mapped results.
	var records = queryResults.asMappedResults();
	
	// Initialize the file contents.
	var csv = "data:text/plain;charset=utf-8,";

	// Get the column names.
	var columnNames = Object.keys( records[0] );	
	var row = '"' + columnNames.join( '","' ) + '"';
	csv += row + "\r\n";
	
	// Add the records to the file...
	for ( r = 0; r < records.length; r++ ) {

		// Get the record.
		var record = records[r];
		
		var values = [];

		// Loop over the columns...
		for ( c = 0; c < columnNames.length; c++ ) {

			// Get the column name.
			var column = columnNames[c];

			// Get the column value.
			var value = record[column];
			if ( value != null ) {
				value = value.toString();
			} else {
				value = '';
			}

			// Add the column value.
			values.push( '"' + value + '"' );		     

		}
		
		var row = values.join( ',' );
		csv += row + "\r\n";		

	}
	
	// Add an inline HTML field so that JavaScript can be injected.
	var jsField = form.addField(
		{
			id: 'custpage_field_js_export_csv',
			type: serverWidget.FieldType.INLINEHTML,
			label: 'Javascript'
		}								
	);
	
	// Create JavaScript to download the file.
	var js = '<script>\r\n';	
	js += 'var encodedUri = encodeURI( `' + csv + '` );\r\n';
	js += 'window.open( encodedUri );\r\n'
	js += '</script>\r\n';	
	
	// Add Javascript.
	jsField.defaultValue = js;

	// Add a "Run Query" submit button.
	form.addSubmitButton( { label: 'Run Query' } );			

	// Add a "Load Query" button.
	loadQueryButtonAdd( form );

	// Add a "Save Query" button.
	saveQueryButtonAdd( form );	

	// Add the query field.
	queryFieldAdd( context, form );		
	
	// Add a "Status" field.
	var statusField = form.addField(
		{
			id: 'custpage_field_status',
			type: serverWidget.FieldType.TEXT,
			label: 'Status'
		}								
	);		
	
	// Set the field's value.
	statusField.defaultValue = 'Exported';	

}


function javascriptAdd( context, form ) {

	// Add an inline HTML field so that JavaScript can be injected.
	var jsField = form.addField(
		{
			id: 'custpage_field_js',
			type: serverWidget.FieldType.INLINEHTML,
			label: 'Javascript'
		}								
	);
	
	// Add Javascript...
	jsField.defaultValue = '<script>\r\n';
	
	// Adjust the size of the textareas.
	jsField.defaultValue += 'document.getElementById("custpage_field_query").rows=20;\r\n';
	if ( context.request.parameters.custpage_field_action == 'run-query' ) {	
		jsField.defaultValue += 'document.getElementById("custpage_field_results").rows=20;\r\n';
	}		
		
	// Use jQuery to modify the tab key's behavior when in the query textarea.
	// This allows the user to use the tab key when editing a query.
	// Source: https://stackoverflow.com/questions/6140632/how-to-handle-tab-in-textarea		
	jsField.defaultValue += 'window.jQuery = window.$ = jQuery;\r\n';			
	jsField.defaultValue += '$(\'textarea\').keydown(function(e) {\r\n';
	jsField.defaultValue += 'if(e.keyCode === 9) {\r\n';
	jsField.defaultValue += 'var start = this.selectionStart;\r\n';
	jsField.defaultValue += 'var end = this.selectionEnd;\r\n';
	jsField.defaultValue += 'var $this = $(this);\r\n';
	jsField.defaultValue += 'var value = $this.val();\r\n';
	jsField.defaultValue += '$this.val(value.substring(0, start)';
	jsField.defaultValue += '+ "\t"';
	jsField.defaultValue += '+ value.substring(end));\r\n';
	jsField.defaultValue += 'this.selectionStart = this.selectionEnd = start + 1;\r\n';
	jsField.defaultValue += 'e.preventDefault();\r\n';
	jsField.defaultValue += '}\r\n';
	jsField.defaultValue += '});\r\n';	
	
	jsField.defaultValue += '</script>';

}


function loadQueryButtonAdd( form ) {

	// If no SuiteQL Scripts folder is available, then abort.
	if ( sqlFolderID === null ) { return; }
	
	// Get the files in the SQL folder.
	files = sqlFolderFilesGet();
	
	// If no files are available, abort.
	if ( files === null ) { return; }	

	// Client-side script that will be run when the Load button is clicked.
	var loadFunction =
		'document.getElementById(\'custpage_field_action\').value = (\'load-step-1\');'
		+ 'document.main_form.submit();';

	// Add a "Load Query" button.	
	form.addButton( 
		{
			id: 'custpage_button_add',
			label: 'Load Query',
			functionName: loadFunction
		} 
	);
			
}


function loadQueryFormPrep( context, form ) {

	// Add a "Save" submit button.
	form.addSubmitButton( { label: 'Load' } );	
	
	// Get the action field.
	var actionField = form.getField( { id : 'custpage_field_action' } );	
	
	// Set the value for the action field.
	actionField.defaultValue = 'load-step-2';	

	// Add a "Folder" field.
	var foldernameField = form.addField(
		{
			id: 'custpage_field_folder',
			type: serverWidget.FieldType.TEXT,
			label: 'Folder'
		}								
	);	
	
	// Set the field's value.
	foldernameField.defaultValue = sqlFolderName;
	
	// Disable the field.
	foldernameField.updateDisplayType(
		{
			displayType: serverWidget.FieldDisplayType.DISABLED
		}
	);		
						
	// Add a "Select A File" field.
	var fileIDField = form.addField(
		{
			id: 'custpage_field_fileid',
			type: serverWidget.FieldType.SELECT,
			label: 'Select A File'
		}								
	);		
	
	// Add the files as field options...
	for ( i = 0; i < sqlFiles.length; i++ ) {

		// Get the file.
		var file = sqlFiles[i];	
	
		// Add the option.
		fileIDField.addSelectOption(
			{
				value : file['id'],
				text : file['name']
			}
		);		
		
	}			
					
}


function loadQueryProcess( context, form ) {

	// Load the file.
	var fileObj = file.load( 
		{ 
			id: context.request.parameters.custpage_field_fileid 
		}
	);

	// Add a "Run Query" submit button.
	form.addSubmitButton( { label: 'Run Query' } );			

	// Add a "Load Query" button.
	loadQueryButtonAdd( form );		
	
	// Add a "Save Query" button.
	saveQueryButtonAdd( form );			

	// Add the query field.
	queryFieldAdd( context, form );	
	
	// Get the query field.
	var queryField = form.getField( { id : 'custpage_field_query' } );			
	
	// Set the field's value.
	queryField.defaultValue = fileObj.getContents();		

}


function queryFieldAdd( context, form ) {

	// Add the query field.
	var queryField = form.addField(
		{
			id: 'custpage_field_query',
			type: serverWidget.FieldType.LONGTEXT,
			label: 'Query'
		}								
	);
	
	// Make the query field required.
	queryField.isMandatory = true;	
	
	// If the form has been submitted...
	if ( context.request.method == 'POST' ) {	
			
		// Set the field's default value.
		queryField.defaultValue = context.request.parameters.custpage_field_query;	
		
	}
			
}


function queryRun( context, form ) {

	// Add a "Run Query" submit button.
	form.addSubmitButton( { label: 'Run Query' } );			

	// Add a "Load Query" button.
	loadQueryButtonAdd( form );

	// Add a "Save Query" button.
	saveQueryButtonAdd( form );	
	
	// Add the query field.
	queryFieldAdd( context, form );	

	// Add the Results field.
	var resultsField = form.addField(
		{
			id: 'custpage_field_results',
			type: serverWidget.FieldType.LONGTEXT,
			label: 'Results'
		}								
	);			

	try {

		// Run the query.
		var beginTime = new Date().getTime();
		var queryResults = query.runSuiteQL(
			{
				query: context.request.parameters.custpage_field_query
			}
		); 	
		var endTime = new Date().getTime();
		var elapsedTime = endTime - beginTime ;						
	
		// Get the mapped results.		
		var records = queryResults.asMappedResults();
	
		// Adjust the label so that it includes the number of results.
		resultsField.label = queryResults.results.length + ' Results (JSON)';					
	
		// If records were returned...
		if ( records.length > 0 ) {
		
			// Add an "Export Results" button.	
			exportResultsButtonAdd( form );			

			// Create a sublist for the results.
			var resultsSublist = form.addSublist(
				{ 
					id : 'results_sublist', 
					label : 'Results (' + records.length + ' records retrieved in ' + elapsedTime + 'ms)', 
					type : serverWidget.SublistType.LIST 
				}
			);

			// Get the column names.
			var columnNames = Object.keys( records[0] );

			// Loop over the column names...
			for ( i = 0; i < columnNames.length; i++ ) {

				// Add the column to the sublist as a field.
				resultsSublist.addField(
					{ 
						id: 'custpage_results_sublist_col_' + i,
						type: serverWidget.FieldType.TEXT,
						label: columnNames[i]
					}
				);

			}

			// Add the records to the sublist...
			for ( r = 0; r < records.length; r++ ) {

				// Get the record.
				var record = records[r];

				// Loop over the columns...
				for ( c = 0; c < columnNames.length; c++ ) {

					// Get the column name.
					var column = columnNames[c];

					// Get the column value.
					var value = record[column];
					
					// If the column has a value...
					if ( value != null ) {
					
						// Get the value as a string.
						value = value.toString();
						
						// If the value is too long to be displayed in the sublist...
						if ( value.length > 300 ) {
						
							// Truncate the value.
							value = value.substring( 0, 297 ) + '...';			
							
						}

						// Add the column value.		
						resultsSublist.setSublistValue(
							{
								id : 'custpage_results_sublist_col_' + c,
								line : r,
								value : value
							}
						);        

					}	
					
				}

			}

		}
		
		// JSON encode the recordset.
		var recordsJSON = JSON.stringify( records, null, 2 );
		
		// If the value can be displayed in a field...
		if ( recordsJSON.length <= 100000 ) {				

			// Display the entire recordset.
			resultsField.defaultValue = recordsJSON;	
			
		} else {
				
			// Display only the first record.
			recordsJSON = 'Example Result:\r\n' + JSON.stringify( records[0], null, 2 );
			resultsField.defaultValue = recordsJSON;
		
		}							

	} catch( e ) {	

		// Update the results field to reflect the error.
		resultsField.label = 'Error';			
		resultsField.defaultValue = e.message;			
		
	}

}


function saveQueryButtonAdd( form ) {

	// If no SuiteQL Scripts folder is available, then abort.
	if ( sqlFolderID === null ) { return; }

	// Client-side script that will be run when the Save button is clicked.
	var saveFunction =
		'document.getElementById(\'custpage_field_action\').value = (\'save-step-1\');'
		+ 'document.main_form.submit();';			
	
	// Add a "Save Query" button.	
	form.addButton( 
		{
			id: 'custpage_button_add',
			label: 'Save Query',
			functionName: saveFunction
		} 
	);
			
}


function saveQueryFormPrep( context, form ) {

	// Add a "Save" submit button.
	form.addSubmitButton( { label: 'Save' } );	
	
	// Get the action field.
	var actionField = form.getField( { id : 'custpage_field_action' } );	
	
	// Set the value for the action field.
	actionField.defaultValue = 'save-step-2';	
	
	// Add the query field.
	queryFieldAdd( context, form );		

	// Add a "Folder" field.
	var foldernameField = form.addField(
		{
			id: 'custpage_field_folder',
			type: serverWidget.FieldType.TEXT,
			label: 'Folder'
		}								
	);	
	
	// Set the field's value.
	foldernameField.defaultValue = sqlFolderName;
	
	// Disable the field.
	foldernameField.updateDisplayType(
		{
			displayType: serverWidget.FieldDisplayType.DISABLED
		}
	);									

	// Add a "File Name" field.
	var filenameField = form.addField(
		{
			id: 'custpage_field_filename',
			type: serverWidget.FieldType.TEXT,
			label: 'File Name'
		}								
	);							
					
}


function saveQueryProcess( context, form ) {

	// Create the file.
	var fileObj = file.create( 
		{
			name: context.request.parameters.custpage_field_filename,
			contents: context.request.parameters.custpage_field_query,
			description: 'SuiteQL',
			fileType: file.Type.PLAINTEXT,
			folder: sqlFolderID,
			isOnline: false
		} 
	);
	
	// Save the file and get its ID.
	var fileID = fileObj.save();
	
	// Add a "Run Query" submit button.
	form.addSubmitButton( { label: 'Run Query' } );			

	// Add a "Load Query" button.
	loadQueryButtonAdd( form );			

	// Add the query field.
	queryFieldAdd( context, form );		
	
	// Add a "Status" field.
	var statusField = form.addField(
		{
			id: 'custpage_field_status',
			type: serverWidget.FieldType.TEXT,
			label: 'Status'
		}								
	);		
	
	// Set the field's value.
	statusField.defaultValue = 'Saved';		

}


function sqlFolderFilesGet() {

	// If there is no SQL folder, then abort.
	if ( sqlFolderID === null ) { return; }

	// Create the query.
	var sql = 'SELECT ID, Name ';
	sql += 'FROM File ';
	sql += 'WHERE ( Folder = ' + sqlFolderID + ' ) ';
	sql += 'ORDER BY Name';
	
	// Execute the query.
	var queryResults = query.runSuiteQL( { query: sql } ); 	
	
	// Get the results.
	var records = queryResults.asMappedResults();

	// If files were found...
	if ( records.length > 0 ) {
		return records;
	} else {
		return null;
	}	

}


function sqlFolderGet() {

	// Create the query.
	var sql = 'SELECT ID ';
	sql += 'FROM MediaItemFolder ';
	sql += 'WHERE ( IsTopLevel = \'T\' ) ';
	sql += 'AND ( Name = \'' + sqlFolderName + '\' )';
	
	// Execute the query.
	var queryResults = query.runSuiteQL( { query: sql } ); 	
	
	// Get the results.
	var records = queryResults.asMappedResults();

	// If the folder was found...
	if ( records.length == 1 ) {
		return records[0]['id'];
	} else {
		return null;
	}	

}

