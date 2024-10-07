# Meeting1

Meeting object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | The Position of the Meeting(Can only be updated if the Meeting is the first Meeting in the series) | [optional] 
**title** | **str** | The Title of the Meeting | [optional] 
**location** | **str** | The Location of the Meeting | [optional] 
**minutes** | **str** | The Minutes of the Meeting | [optional] 
**overview** | **str** | The Description of the Meeting | [optional] 
**occurred** | **bool** | The Occurred status of the Meeting | [optional] [default to False]
**starts_at** | **str** | The Start Time of the Meeting | [optional] 
**ends_at** | **str** | The Finish Time of the Meeting | [optional] 
**time_zone** | **str** | The Timezone of the Meeting | [optional] 
**is_private** | **bool** | The Private status of the Meeting | [optional] 
**conclusion** | **str** | The Conclusion of the Meeting | [optional] 
**is_draft** | **bool** | The Draft status of the Meeting | [optional] [default to False]
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.meeting1 import Meeting1

# TODO update the JSON string below
json = "{}"
# create an instance of Meeting1 from a JSON string
meeting1_instance = Meeting1.from_json(json)
# print the JSON string representation of the object
print(Meeting1.to_json())

# convert the object into a dict
meeting1_dict = meeting1_instance.to_dict()
# create an instance of Meeting1 from a dict
meeting1_from_dict = Meeting1.from_dict(meeting1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


