# Body53


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**payment_application_line_item** | [**PaymentApplicationOwnerInvoiceLineItem**](PaymentApplicationOwnerInvoiceLineItem.md) |  | 

## Example

```python
from procore_sdk.models.body53 import Body53

# TODO update the JSON string below
json = "{}"
# create an instance of Body53 from a JSON string
body53_instance = Body53.from_json(json)
# print the JSON string representation of the object
print(Body53.to_json())

# convert the object into a dict
body53_dict = body53_instance.to_dict()
# create an instance of Body53 from a dict
body53_from_dict = Body53.from_dict(body53_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


