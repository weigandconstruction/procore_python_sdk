# Body62


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Meetings belongs to | 
**meeting** | [**Meeting1**](Meeting1.md) |  | 
**attachments** | **List[str]** | Meeting Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.body62 import Body62

# TODO update the JSON string below
json = "{}"
# create an instance of Body62 from a JSON string
body62_instance = Body62.from_json(json)
# print the JSON string representation of the object
print(Body62.to_json())

# convert the object into a dict
body62_dict = body62_instance.to_dict()
# create an instance of Body62 from a dict
body62_from_dict = Body62.from_dict(body62_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


