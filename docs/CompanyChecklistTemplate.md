# CompanyChecklistTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**inspection_type** | [**InspectionType2**](InspectionType2.md) |  | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**deletable** | **bool** | Deletable | [optional] 

## Example

```python
from procore_sdk.models.company_checklist_template import CompanyChecklistTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyChecklistTemplate from a JSON string
company_checklist_template_instance = CompanyChecklistTemplate.from_json(json)
# print the JSON string representation of the object
print(CompanyChecklistTemplate.to_json())

# convert the object into a dict
company_checklist_template_dict = company_checklist_template_instance.to_dict()
# create an instance of CompanyChecklistTemplate from a dict
company_checklist_template_from_dict = CompanyChecklistTemplate.from_dict(company_checklist_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


