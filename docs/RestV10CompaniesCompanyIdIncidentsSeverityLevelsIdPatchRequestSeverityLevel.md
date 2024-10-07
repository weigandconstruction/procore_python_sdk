# RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel

Severity Level object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Incident Severity Level | [optional] 
**email_trigger** | **bool** | Indicates whether an email should be sent | [optional] 
**push_notification_trigger** | **bool** | Indicates whether a push notification should be sent | [optional] 
**alert_recipient_ids** | **List[int]** | IDs of Users that should receive notifications | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_incidents_severity_levels_id_patch_request_severity_level import RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel from a JSON string
rest_v10_companies_company_id_incidents_severity_levels_id_patch_request_severity_level_instance = RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel.to_json())

# convert the object into a dict
rest_v10_companies_company_id_incidents_severity_levels_id_patch_request_severity_level_dict = rest_v10_companies_company_id_incidents_severity_levels_id_patch_request_severity_level_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel from a dict
rest_v10_companies_company_id_incidents_severity_levels_id_patch_request_severity_level_from_dict = RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel.from_dict(rest_v10_companies_company_id_incidents_severity_levels_id_patch_request_severity_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


