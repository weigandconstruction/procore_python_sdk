# Body93


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **List[str]** | Direct Cost Item attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**direct_cost** | [**DirectCostItem1**](DirectCostItem1.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body93 import Body93

# TODO update the JSON string below
json = "{}"
# create an instance of Body93 from a JSON string
body93_instance = Body93.from_json(json)
# print the JSON string representation of the object
print(Body93.to_json())

# convert the object into a dict
body93_dict = body93_instance.to_dict()
# create an instance of Body93 from a dict
body93_from_dict = Body93.from_dict(body93_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


