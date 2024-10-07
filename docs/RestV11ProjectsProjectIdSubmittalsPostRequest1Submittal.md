# RestV11ProjectsProjectIdSubmittalsPostRequest1Submittal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_delivery_date** | **date** | The Actual Delivery Date of the Submittal *This field can only be set if the project has submittal delivery information enabled | [optional] 
**attachments** | **List[str]** | Submittal attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**confirmed_delivery_date** | **date** | The Confirmed Delivery Date of the Submittal *This field can only be set if the project has submittal delivery information enabled | [optional] 
**cost_code_id** | **int** | The ID of the Cost Code of the Submittal *This field can only be set by admins | [optional] 
**custom_textarea_1** | **str** | *This field can only be set by admins  | [optional] 
**custom_textfield_1** | **str** | *This field can only be set by admins  | [optional] 
**description** | **str** | The Description of the Submittal | [optional] 
**design_team_review_time** | **int** | The Design Team Review Time of the Submittal (in days) *This field can only be set if the project has schedule calculations enabled | [optional] 
**distribution_member_ids** | **List[int]** | The IDs of the Distribution Members of the Submittal | [optional] 
**due_date** | **date** | The Due Date of the Submittal *This field is not available to be set if sequential approvers is enabled | [optional] 
**internal_review_time** | **int** | The Internal Review Time of the Submtital (in days) *This field can only be set if the project has schedule calculations enabled | [optional] 
**issue_date** | **date** | The Issue Date of the Submittal *This field can only be set by admins | [optional] 
**lead_time** | **int** | The Lead Time of the Submittal (in days) *This field can only be set by admins or if the project has schedule calculations enabled | [optional] 
**location_id** | **int** | The Location of the Submittal | [optional] 
**number** | **str** | The Number of the Submittal | 
**private** | **bool** | Whether the Submittal is Private or not | [optional] 
**prostore_file_ids** | **List[int]** | An array of Prostore File IDs. The Prostore Files will be associated with the Submittal as attachments. | [optional] 
**received_date** | **date** | The Received Date of the Submittal *This field can only be set by admins | [optional] 
**received_from_id** | **int** | The Received From of the Submittal | [optional] 
**required_on_site_date** | **date** | The Required On Site Date of the Submittal *This field can only be set by admins or if the project has schedule calculations enabled | [optional] 
**responsible_contractor_id** | **int** | The Responsible Contractor of the Submittal | [optional] 
**revision** | **str** | The Revision of the Submittal | [optional] 
**scheduled_task_key** | **str** | The key of the Scheduled Task of the Submittal. Note that use of this parameter is deprecated. Please use &#x60;scheduled_task_id&#x60; instead. *This field can only be set if the project has submittal delivery information enabled and the user has permissions to view the calendar tool | [optional] 
**scheduled_task_id** | **int** | The ID of the Scheduled Task of the Submittal *This field can only be set if the project has submittal delivery information enabled and the user has permissions to view the calendar tool | [optional] 
**source_submittal_log_id** | **int** | The ID of the Source Submittal. *By setting this field, the submittal will be created as a revision of source submittal. | [optional] 
**specification_section_id** | **int** | The ID of the Specification Section of the Submittal | [optional] 
**status_id** | **int** | The ID of the Submittal Status of the Submittal *This field can only be set by admins | [optional] 
**sub_job_id** | **int** | The ID of the Sub Job of the Submittal | [optional] 
**submit_by** | **date** | The Submit By Date of the Submittal *This field can only be set by admins | [optional] 
**submittal_manager_id** | **int** | The ID of the Submittal Manager of the Submittal *This field can only be set by admins | [optional] 
**submittal_package_id** | **int** | The ID of the Submittal Package of the Submittal *This field can only be set by admins | [optional] 
**title** | **str** | The Title of the Submittal | [optional] 
**type** | **str** | The Submittal Type of the Submittal | [optional] 
**workflow_data** | **List[List[RestV11ProjectsProjectIdSubmittalsPostRequest1SubmittalWorkflowDataInnerInner]]** |  | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_submittals_post_request1_submittal import RestV11ProjectsProjectIdSubmittalsPostRequest1Submittal

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsPostRequest1Submittal from a JSON string
rest_v11_projects_project_id_submittals_post_request1_submittal_instance = RestV11ProjectsProjectIdSubmittalsPostRequest1Submittal.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsPostRequest1Submittal.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_post_request1_submittal_dict = rest_v11_projects_project_id_submittals_post_request1_submittal_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsPostRequest1Submittal from a dict
rest_v11_projects_project_id_submittals_post_request1_submittal_from_dict = RestV11ProjectsProjectIdSubmittalsPostRequest1Submittal.from_dict(rest_v11_projects_project_id_submittals_post_request1_submittal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


