# Body61


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Meetings belongs to | 
**meeting** | [**Meeting**](Meeting.md) |  | 
**attachments** | **List[str]** | Meeting Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**prostore_file_ids** | **List[int]** | Ids of meeting attachment files Prostore file IDs (Not to be used if other attachment types are included) | [optional] 

## Example

```python
from procore_sdk.models.body61 import Body61

# TODO update the JSON string below
json = "{}"
# create an instance of Body61 from a JSON string
body61_instance = Body61.from_json(json)
# print the JSON string representation of the object
print(Body61.to_json())

# convert the object into a dict
body61_dict = body61_instance.to_dict()
# create an instance of Body61 from a dict
body61_from_dict = Body61.from_dict(body61_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


