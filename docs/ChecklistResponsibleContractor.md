# ChecklistResponsibleContractor

Vendor responsible for the work being inspected

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from procore_sdk.models.checklist_responsible_contractor import ChecklistResponsibleContractor

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistResponsibleContractor from a JSON string
checklist_responsible_contractor_instance = ChecklistResponsibleContractor.from_json(json)
# print the JSON string representation of the object
print(ChecklistResponsibleContractor.to_json())

# convert the object into a dict
checklist_responsible_contractor_dict = checklist_responsible_contractor_instance.to_dict()
# create an instance of ChecklistResponsibleContractor from a dict
checklist_responsible_contractor_from_dict = ChecklistResponsibleContractor.from_dict(checklist_responsible_contractor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


