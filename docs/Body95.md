# Body95


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **List[str]** | Direct Cost Item attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**item** | [**DirectCostItem2**](DirectCostItem2.md) |  | 

## Example

```python
from procore_sdk.models.body95 import Body95

# TODO update the JSON string below
json = "{}"
# create an instance of Body95 from a JSON string
body95_instance = Body95.from_json(json)
# print the JSON string representation of the object
print(Body95.to_json())

# convert the object into a dict
body95_dict = body95_instance.to_dict()
# create an instance of Body95 from a dict
body95_from_dict = Body95.from_dict(body95_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


