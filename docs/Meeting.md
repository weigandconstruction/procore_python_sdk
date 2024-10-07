# Meeting

Meeting object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | The Position of the Meeting | [default to 1]
**title** | **str** | The Title of the Meeting | [optional] 
**location** | **str** | The Location of the Meeting | [optional] 
**minutes** | **str** | The Minutes of the Meeting | [optional] 
**overview** | **str** | The Description of the Meeting | [optional] 
**occurred** | **bool** | The Occurred status of the Meeting | [optional] [default to False]
**starts_at** | **str** | The Start Time of the Meeting | 
**ends_at** | **str** | The Finish Time of the Meeting | 
**time_zone** | **str** | The Timezone of the Meeting | [optional] 
**is_private** | **bool** | The Private status of the Meeting | [optional] 
**conclusion** | **str** | The Conclusion of the Meeting | [optional] 
**is_draft** | **bool** | The Draft status of the Meeting | [optional] 
**attendees** | **List[int]** | An array of the IDs of the Attendees of the Meeting | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.meeting import Meeting

# TODO update the JSON string below
json = "{}"
# create an instance of Meeting from a JSON string
meeting_instance = Meeting.from_json(json)
# print the JSON string representation of the object
print(Meeting.to_json())

# convert the object into a dict
meeting_dict = meeting_instance.to_dict()
# create an instance of Meeting from a dict
meeting_from_dict = Meeting.from_dict(meeting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


