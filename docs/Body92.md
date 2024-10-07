# Body92


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **List[str]** | Direct Cost Item attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**direct_cost** | [**DirectCostItem**](DirectCostItem.md) |  | 

## Example

```python
from procore_sdk.models.body92 import Body92

# TODO update the JSON string below
json = "{}"
# create an instance of Body92 from a JSON string
body92_instance = Body92.from_json(json)
# print the JSON string representation of the object
print(Body92.to_json())

# convert the object into a dict
body92_dict = body92_instance.to_dict()
# create an instance of Body92 from a dict
body92_from_dict = Body92.from_dict(body92_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


