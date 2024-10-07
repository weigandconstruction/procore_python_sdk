# RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**question_date** | **datetime** | Date | [optional] 
**plain_text_body** | **str** | Plain text body | [optional] 
**rich_text_body** | **str** | Rich text body | [optional] 
**created_by** | **str** | Creator name | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | Attachments | [optional] 
**answers** | [**List[RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner]**](RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner.md) | Answers | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner import RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInner from a JSON string
rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_instance = RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_dict = rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInner from a dict
rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_from_dict = RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInner.from_dict(rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


