# RestV11ProjectsProjectIdChecklistListTemplatesIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**deletable** | **bool** | Deletable | [optional] 
**company_description** | **str** | Company Description | [optional] 
**description** | **str** | Description | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 
**synced_to** | [**ProjectChecklistTemplateSyncedTo**](ProjectChecklistTemplateSyncedTo.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 
**company_attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 
**sections** | [**List[RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInner]**](RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInner.md) | Sections | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_checklist_list_templates_id_get200_response import RestV11ProjectsProjectIdChecklistListTemplatesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdChecklistListTemplatesIdGet200Response from a JSON string
rest_v11_projects_project_id_checklist_list_templates_id_get200_response_instance = RestV11ProjectsProjectIdChecklistListTemplatesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdChecklistListTemplatesIdGet200Response.to_json())

# convert the object into a dict
rest_v11_projects_project_id_checklist_list_templates_id_get200_response_dict = rest_v11_projects_project_id_checklist_list_templates_id_get200_response_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdChecklistListTemplatesIdGet200Response from a dict
rest_v11_projects_project_id_checklist_list_templates_id_get200_response_from_dict = RestV11ProjectsProjectIdChecklistListTemplatesIdGet200Response.from_dict(rest_v11_projects_project_id_checklist_list_templates_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


