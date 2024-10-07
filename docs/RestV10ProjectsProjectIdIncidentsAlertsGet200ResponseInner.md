# RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Incident Alert ID | [optional] 
**event_id** | **int** | Incident Alert Event ID | [optional] 
**emailed_at** | **datetime** | Timestamp of email delivery | [optional] 
**filing_type** | [**IncidentFilingType**](IncidentFilingType.md) |  | [optional] 
**injury** | [**RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjury**](RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjury.md) |  | [optional] 
**pushed_at** | **datetime** | Timestamp of when the push notification delivery | [optional] 
**recipient** | [**RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner**](RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner.md) |  | [optional] 
**severity_level** | [**SeverityLevel**](SeverityLevel.md) |  | [optional] 
**triggered_at** | **datetime** | Timestamp of when the alert was triggered | [optional] 
**triggered_by** | [**RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner**](RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_incidents_alerts_get200_response_inner import RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_incidents_alerts_get200_response_inner_instance = RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_incidents_alerts_get200_response_inner_dict = rest_v10_projects_project_id_incidents_alerts_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInner from a dict
rest_v10_projects_project_id_incidents_alerts_get200_response_inner_from_dict = RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInner.from_dict(rest_v10_projects_project_id_incidents_alerts_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


