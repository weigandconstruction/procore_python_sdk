# Body21


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**commitment_id** | **int** | Commitment ID | 
**attachments** | **List[str]** | Requisition (Subcontractor Invoice) attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**requisition** | [**RequisitionSubcontractorInvoice2**](RequisitionSubcontractorInvoice2.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body21 import Body21

# TODO update the JSON string below
json = "{}"
# create an instance of Body21 from a JSON string
body21_instance = Body21.from_json(json)
# print the JSON string representation of the object
print(Body21.to_json())

# convert the object into a dict
body21_dict = body21_instance.to_dict()
# create an instance of Body21 from a dict
body21_from_dict = Body21.from_dict(body21_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


