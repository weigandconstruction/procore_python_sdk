# Body109


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**contract_id** | **int** | Contract ID | 
**attachments** | **List[str]** | Contract payment attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**contract_payment** | [**ContractPayment**](ContractPayment.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body109 import Body109

# TODO update the JSON string below
json = "{}"
# create an instance of Body109 from a JSON string
body109_instance = Body109.from_json(json)
# print the JSON string representation of the object
print(Body109.to_json())

# convert the object into a dict
body109_dict = body109_instance.to_dict()
# create an instance of Body109 from a dict
body109_from_dict = Body109.from_dict(body109_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


