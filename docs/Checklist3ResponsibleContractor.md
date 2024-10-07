# Checklist3ResponsibleContractor

Vendor responsible for the work being inspected

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from procore_sdk.models.checklist3_responsible_contractor import Checklist3ResponsibleContractor

# TODO update the JSON string below
json = "{}"
# create an instance of Checklist3ResponsibleContractor from a JSON string
checklist3_responsible_contractor_instance = Checklist3ResponsibleContractor.from_json(json)
# print the JSON string representation of the object
print(Checklist3ResponsibleContractor.to_json())

# convert the object into a dict
checklist3_responsible_contractor_dict = checklist3_responsible_contractor_instance.to_dict()
# create an instance of Checklist3ResponsibleContractor from a dict
checklist3_responsible_contractor_from_dict = Checklist3ResponsibleContractor.from_dict(checklist3_responsible_contractor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


