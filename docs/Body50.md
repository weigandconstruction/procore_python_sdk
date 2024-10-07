# Body50


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**attachments** | **List[str]** | Payment application attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**payment_application** | [**PaymentApplicationOwnerInvoice**](PaymentApplicationOwnerInvoice.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body50 import Body50

# TODO update the JSON string below
json = "{}"
# create an instance of Body50 from a JSON string
body50_instance = Body50.from_json(json)
# print the JSON string representation of the object
print(Body50.to_json())

# convert the object into a dict
body50_dict = body50_instance.to_dict()
# create an instance of Body50 from a dict
body50_from_dict = Body50.from_dict(body50_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


