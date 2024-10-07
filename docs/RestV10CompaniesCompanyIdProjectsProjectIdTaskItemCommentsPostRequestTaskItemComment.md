# RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The message of the comment | [optional] 
**status** | **str** | The status of the task item at the time the comment is created. Standard users who are assigned to the task item cannot change the status to closed or void. | [optional] 
**task_item_id** | **int** | The task_item associated with the comment | 
**attachments** | **List[str]** | Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_projects_project_id_task_item_comments_post_request_task_item_comment import RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment from a JSON string
rest_v10_companies_company_id_projects_project_id_task_item_comments_post_request_task_item_comment_instance = RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment.to_json())

# convert the object into a dict
rest_v10_companies_company_id_projects_project_id_task_item_comments_post_request_task_item_comment_dict = rest_v10_companies_company_id_projects_project_id_task_item_comments_post_request_task_item_comment_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment from a dict
rest_v10_companies_company_id_projects_project_id_task_item_comments_post_request_task_item_comment_from_dict = RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment.from_dict(rest_v10_companies_company_id_projects_project_id_task_item_comments_post_request_task_item_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


