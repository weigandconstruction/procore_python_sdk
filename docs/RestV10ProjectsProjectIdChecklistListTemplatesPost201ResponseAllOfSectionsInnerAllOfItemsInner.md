# RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInnerAllOfItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**section_id** | **int** | Checklist Template Section ID | [optional] 
**position** | **int** | Position | [optional] 
**response_set** | [**ChecklistTemplateItemResponseSet1**](ChecklistTemplateItemResponseSet1.md) |  | [optional] 
**details** | **str** | Additional information about item | [optional] 
**synced_to** | [**RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInnerAllOfSyncedTo**](RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInnerAllOfSyncedTo.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_sections_inner_all_of_items_inner import RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInnerAllOfItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInnerAllOfItemsInner from a JSON string
rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_sections_inner_all_of_items_inner_instance = RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInnerAllOfItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInnerAllOfItemsInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_sections_inner_all_of_items_inner_dict = rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_sections_inner_all_of_items_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInnerAllOfItemsInner from a dict
rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_sections_inner_all_of_items_inner_from_dict = RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInnerAllOfItemsInner.from_dict(rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_sections_inner_all_of_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


