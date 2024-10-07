# RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**position** | **int** | Position | [optional] 
**items** | [**List[RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInnerAllOfItemsInner]**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInnerAllOfItemsInner.md) |  | [optional] 
**synced_to** | [**RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfSyncedTo**](RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfSyncedTo.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_sections_inner import RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInner from a JSON string
rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_sections_inner_instance = RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_sections_inner_dict = rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_sections_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInner from a dict
rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_sections_inner_from_dict = RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInner.from_dict(rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_sections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


