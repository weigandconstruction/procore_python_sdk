# ChecklistSignatureRequestSignatory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the user. | [optional] 
**login** | **str** | The email address of the user that is used to log in. | [optional] 
**name** | **str** | The name of the user. | [optional] 
**company_name** | **str** | User&#39;s Company Name | [optional] 

## Example

```python
from procore_sdk.models.checklist_signature_request_signatory import ChecklistSignatureRequestSignatory

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSignatureRequestSignatory from a JSON string
checklist_signature_request_signatory_instance = ChecklistSignatureRequestSignatory.from_json(json)
# print the JSON string representation of the object
print(ChecklistSignatureRequestSignatory.to_json())

# convert the object into a dict
checklist_signature_request_signatory_dict = checklist_signature_request_signatory_instance.to_dict()
# create an instance of ChecklistSignatureRequestSignatory from a dict
checklist_signature_request_signatory_from_dict = ChecklistSignatureRequestSignatory.from_dict(checklist_signature_request_signatory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


