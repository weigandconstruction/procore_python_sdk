# RestV11ProjectsProjectIdProjectTimecardEntriesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hours** | **str** | Total number of hours worked (excluding breaks) for the timecard entry. This property is not required if the timesheet time entry is configured for start time and stop time. | [optional] 
**lunch_time** | **str** | The duration of the lunch break, in minutes, for the Timecard Entry. This property is only required if the timesheet time entry is configured for start time and stop time. | [optional] 
**time_in** | **str** | The start time of the Timecard Entry in ISO 8601 format. This property is only required if the timesheet time entry is configured for start time and stop time. | [optional] 
**time_out** | **str** | The stop time of the Timecard Entry in ISO 8601 format. This property is only required if the timesheet time entry is configured for start time and stop time. | [optional] 
**billable** | **bool** | The billable status of the Timecard Entry. Must be either true or false. | [optional] [default to False]
**var_date** | **date** | The date of the Timecard Entry in ISO 8601 format. | [optional] 
**description** | **str** | The description of the Timecard Entry. | [optional] 
**timecard_time_type_id** | **int** | The ID of the Timecard Time Type corresponding to the Timecard Entry property. | [optional] 
**timesheet_id** | **int** | The ID of the Timesheet corresponding to the Timecard Entry property. | [optional] 
**cost_code_id** | **int** | The ID of the Cost Code corresponding to the Timecard Entry property. | [optional] 
**sub_job_id** | **int** | The ID of the Subjob corresponding to the Timecard Entry property. | [optional] 
**location_id** | **int** | The ID of the Location corresponding to the Timecard Entry property. | [optional] 
**login_information_id** | **int** | The ID of the Login Information corresponding to the Timecard Entry property. | [optional] 
**party_id** | **int** | The ID of the Party corresponding to the Timecard Entry property. | [optional] 
**origin_id** | **int** | The ID of the related external data. | [optional] 
**origin_data** | **str** | The value of the related external data. | [optional] 
**line_item_type_id** | **int** | The ID of the line item type corresponding to the time card entry. | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_project_timecard_entries_post_request import RestV11ProjectsProjectIdProjectTimecardEntriesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdProjectTimecardEntriesPostRequest from a JSON string
rest_v11_projects_project_id_project_timecard_entries_post_request_instance = RestV11ProjectsProjectIdProjectTimecardEntriesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdProjectTimecardEntriesPostRequest.to_json())

# convert the object into a dict
rest_v11_projects_project_id_project_timecard_entries_post_request_dict = rest_v11_projects_project_id_project_timecard_entries_post_request_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdProjectTimecardEntriesPostRequest from a dict
rest_v11_projects_project_id_project_timecard_entries_post_request_from_dict = RestV11ProjectsProjectIdProjectTimecardEntriesPostRequest.from_dict(rest_v11_projects_project_id_project_timecard_entries_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


