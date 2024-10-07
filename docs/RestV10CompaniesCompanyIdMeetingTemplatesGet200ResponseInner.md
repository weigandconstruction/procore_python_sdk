# RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner

Meeting Template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id | [optional] 
**name** | **str** | Name | [optional] 
**overview** | **str** | Overview | [optional] 
**private** | **bool** | Indicates that this meeting template should be private | [optional] 
**agendas** | [**List[RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInner]**](RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInner.md) | Agendas | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAttachmentsInner.md) | Attachments | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_meeting_templates_get200_response_inner import RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner from a JSON string
rest_v10_companies_company_id_meeting_templates_get200_response_inner_instance = RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_meeting_templates_get200_response_inner_dict = rest_v10_companies_company_id_meeting_templates_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner from a dict
rest_v10_companies_company_id_meeting_templates_get200_response_inner_from_dict = RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner.from_dict(rest_v10_companies_company_id_meeting_templates_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


