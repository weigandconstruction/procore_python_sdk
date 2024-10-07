# RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner

Normal view of task item comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID of the comment | [optional] 
**comment** | **str** | The actual message of the comment | [optional] 
**status** | **str** | The status of the task item at the time this comment was created | [optional] 
**attachments** | [**RestV10WorkOrderContractsPost201ResponseAttachmentsInner**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**created_by** | [**RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInnerCreatedBy**](RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**task_item_id** | **int** | The task item id associated with the comment | [optional] 
**created_at** | **datetime** | The UTC datetime for the creation of the resource in ISO 8601 format. | [optional] 
**updated_at** | **datetime** | The UTC datetime for the last update of the resource in ISO 8601 format. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_projects_project_id_task_item_comments_get200_response_inner import RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_projects_project_id_task_item_comments_get200_response_inner_instance = RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_projects_project_id_task_item_comments_get200_response_inner_dict = rest_v10_companies_company_id_projects_project_id_task_item_comments_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner from a dict
rest_v10_companies_company_id_projects_project_id_task_item_comments_get200_response_inner_from_dict = RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner.from_dict(rest_v10_companies_company_id_projects_project_id_task_item_comments_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


