# RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**official** | **bool** | Official response, true if official | [optional] 
**answer_date** | **datetime** | Date | [optional] 
**plain_text_body** | **str** | Plain text body | [optional] 
**rich_text_body** | **str** | Rich text body | [optional] 
**created_by** | **str** | Creator name | [optional] 
**created_by_id** | **int** | Creator ID | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | Attachments | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_answers_inner import RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner from a JSON string
rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_answers_inner_instance = RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_answers_inner_dict = rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_answers_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner from a dict
rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_answers_inner_from_dict = RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner.from_dict(rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_answers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


