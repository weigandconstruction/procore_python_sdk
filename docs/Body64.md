# Body64


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Meetings belongs to | 
**meeting** | [**Meeting3**](Meeting3.md) |  | 
**attachments** | **List[str]** | Meeting Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.body64 import Body64

# TODO update the JSON string below
json = "{}"
# create an instance of Body64 from a JSON string
body64_instance = Body64.from_json(json)
# print the JSON string representation of the object
print(Body64.to_json())

# convert the object into a dict
body64_dict = body64_instance.to_dict()
# create an instance of Body64 from a dict
body64_from_dict = Body64.from_dict(body64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


