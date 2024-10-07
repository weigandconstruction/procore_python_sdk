# Body52


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**payment_application_markup_line_item** | [**PaymentApplicationOwnerInvoiceMarkupLineItem**](PaymentApplicationOwnerInvoiceMarkupLineItem.md) |  | 

## Example

```python
from procore_sdk.models.body52 import Body52

# TODO update the JSON string below
json = "{}"
# create an instance of Body52 from a JSON string
body52_instance = Body52.from_json(json)
# print the JSON string representation of the object
print(Body52.to_json())

# convert the object into a dict
body52_dict = body52_instance.to_dict()
# create an instance of Body52 from a dict
body52_from_dict = Body52.from_dict(body52_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


