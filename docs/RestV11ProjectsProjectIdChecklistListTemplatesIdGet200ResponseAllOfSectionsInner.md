# RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**position** | **int** | Position | [optional] 
**items** | [**List[RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInner]**](RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInner.md) |  | [optional] 
**synced_to** | [**RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfSyncedTo**](RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfSyncedTo.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_checklist_list_templates_id_get200_response_all_of_sections_inner import RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInner from a JSON string
rest_v11_projects_project_id_checklist_list_templates_id_get200_response_all_of_sections_inner_instance = RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_checklist_list_templates_id_get200_response_all_of_sections_inner_dict = rest_v11_projects_project_id_checklist_list_templates_id_get200_response_all_of_sections_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInner from a dict
rest_v11_projects_project_id_checklist_list_templates_id_get200_response_all_of_sections_inner_from_dict = RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInner.from_dict(rest_v11_projects_project_id_checklist_list_templates_id_get200_response_all_of_sections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


