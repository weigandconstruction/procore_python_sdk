# WbsCodeBulkCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk** | [**List[WbsCodeBulkCreateBulkInner]**](WbsCodeBulkCreateBulkInner.md) |  | 

## Example

```python
from procore_sdk.models.wbs_code_bulk_create import WbsCodeBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WbsCodeBulkCreate from a JSON string
wbs_code_bulk_create_instance = WbsCodeBulkCreate.from_json(json)
# print the JSON string representation of the object
print(WbsCodeBulkCreate.to_json())

# convert the object into a dict
wbs_code_bulk_create_dict = wbs_code_bulk_create_instance.to_dict()
# create an instance of WbsCodeBulkCreate from a dict
wbs_code_bulk_create_from_dict = WbsCodeBulkCreate.from_dict(wbs_code_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


