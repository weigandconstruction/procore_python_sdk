# Checklist1ResponsibleContractor

Vendor responsible for the work being inspected

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from procore_sdk.models.checklist1_responsible_contractor import Checklist1ResponsibleContractor

# TODO update the JSON string below
json = "{}"
# create an instance of Checklist1ResponsibleContractor from a JSON string
checklist1_responsible_contractor_instance = Checklist1ResponsibleContractor.from_json(json)
# print the JSON string representation of the object
print(Checklist1ResponsibleContractor.to_json())

# convert the object into a dict
checklist1_responsible_contractor_dict = checklist1_responsible_contractor_instance.to_dict()
# create an instance of Checklist1ResponsibleContractor from a dict
checklist1_responsible_contractor_from_dict = Checklist1ResponsibleContractor.from_dict(checklist1_responsible_contractor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


