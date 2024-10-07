# RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**inspection_type** | [**InspectionType**](InspectionType.md) |  | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**alternative_response_set_id** | **int** | The ID of the associated Alternative Response Set (if null, the default response set is being used) | [optional] 
**created_by** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 
**response_set** | [**ChecklistAlternativeResponseSet**](ChecklistAlternativeResponseSet.md) |  | [optional] 
**sections** | [**List[RestV10CompaniesCompanyIdChecklistListTemplatesPost201ResponseAllOfSectionsInner]**](RestV10CompaniesCompanyIdChecklistListTemplatesPost201ResponseAllOfSectionsInner.md) | Sections | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_checklist_list_templates_post201_response import RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response from a JSON string
rest_v10_companies_company_id_checklist_list_templates_post201_response_instance = RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_checklist_list_templates_post201_response_dict = rest_v10_companies_company_id_checklist_list_templates_post201_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response from a dict
rest_v10_companies_company_id_checklist_list_templates_post201_response_from_dict = RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response.from_dict(rest_v10_companies_company_id_checklist_list_templates_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


