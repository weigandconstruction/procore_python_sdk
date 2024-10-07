# Body114


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requisition_items** | [**List[RequisitionBulkItemUpdateInner]**](RequisitionBulkItemUpdateInner.md) | Requisition Items | 

## Example

```python
from procore_sdk.models.body114 import Body114

# TODO update the JSON string below
json = "{}"
# create an instance of Body114 from a JSON string
body114_instance = Body114.from_json(json)
# print the JSON string representation of the object
print(Body114.to_json())

# convert the object into a dict
body114_dict = body114_instance.to_dict()
# create an instance of Body114 from a dict
body114_from_dict = Body114.from_dict(body114_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


