# Body51


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**attachments** | **List[str]** | Payment application attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**payment_application** | [**PaymentApplicationOwnerInvoice1**](PaymentApplicationOwnerInvoice1.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body51 import Body51

# TODO update the JSON string below
json = "{}"
# create an instance of Body51 from a JSON string
body51_instance = Body51.from_json(json)
# print the JSON string representation of the object
print(Body51.to_json())

# convert the object into a dict
body51_dict = body51_instance.to_dict()
# create an instance of Body51 from a dict
body51_from_dict = Body51.from_dict(body51_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


