# RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**section_id** | **int** | Checklist Template Section ID | [optional] 
**position** | **int** | Position | [optional] 
**response_set** | [**ChecklistTemplateItemResponseSet**](ChecklistTemplateItemResponseSet.md) |  | [optional] 
**details** | **str** | Additional information about item | [optional] 
**company_template_item_details** | **str** | Details from the company template item | [optional] 
**synced_to** | [**RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInnerAllOfSyncedTo**](RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInnerAllOfSyncedTo.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_checklist_list_templates_id_get200_response_all_of_sections_inner_all_of_items_inner import RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInner from a JSON string
rest_v11_projects_project_id_checklist_list_templates_id_get200_response_all_of_sections_inner_all_of_items_inner_instance = RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_checklist_list_templates_id_get200_response_all_of_sections_inner_all_of_items_inner_dict = rest_v11_projects_project_id_checklist_list_templates_id_get200_response_all_of_sections_inner_all_of_items_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInner from a dict
rest_v11_projects_project_id_checklist_list_templates_id_get200_response_all_of_sections_inner_all_of_items_inner_from_dict = RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInner.from_dict(rest_v11_projects_project_id_checklist_list_templates_id_get200_response_all_of_sections_inner_all_of_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


