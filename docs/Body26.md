# Body26


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**attachments** | **List[str]** | Purchase Order Contract attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**purchase_order_contract** | [**PurchaseOrderContract**](PurchaseOrderContract.md) |  | 

## Example

```python
from procore_sdk.models.body26 import Body26

# TODO update the JSON string below
json = "{}"
# create an instance of Body26 from a JSON string
body26_instance = Body26.from_json(json)
# print the JSON string representation of the object
print(Body26.to_json())

# convert the object into a dict
body26_dict = body26_instance.to_dict()
# create an instance of Body26 from a dict
body26_from_dict = Body26.from_dict(body26_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


