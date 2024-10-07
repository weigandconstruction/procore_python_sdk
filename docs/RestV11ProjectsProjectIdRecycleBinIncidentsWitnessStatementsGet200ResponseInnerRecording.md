# RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Recording ID | [optional] 
**witness_statement_id** | **int** | Witeness Statement ID | [optional] 
**attachment** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecordingAttachment**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecordingAttachment.md) |  | [optional] 
**captured_by** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecordingCapturedBy**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecordingCapturedBy.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_recording import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording from a JSON string
rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_recording_instance = RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording.to_json())

# convert the object into a dict
rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_recording_dict = rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_recording_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording from a dict
rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_recording_from_dict = RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording.from_dict(rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_recording_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


