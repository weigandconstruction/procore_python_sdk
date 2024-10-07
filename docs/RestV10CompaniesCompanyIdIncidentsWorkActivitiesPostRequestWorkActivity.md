# RestV10CompaniesCompanyIdIncidentsWorkActivitiesPostRequestWorkActivity

Work Activity object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Work Activity | 
**active** | **bool** | Flag that denotes if the Work Activity is available for use | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_incidents_work_activities_post_request_work_activity import RestV10CompaniesCompanyIdIncidentsWorkActivitiesPostRequestWorkActivity

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdIncidentsWorkActivitiesPostRequestWorkActivity from a JSON string
rest_v10_companies_company_id_incidents_work_activities_post_request_work_activity_instance = RestV10CompaniesCompanyIdIncidentsWorkActivitiesPostRequestWorkActivity.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdIncidentsWorkActivitiesPostRequestWorkActivity.to_json())

# convert the object into a dict
rest_v10_companies_company_id_incidents_work_activities_post_request_work_activity_dict = rest_v10_companies_company_id_incidents_work_activities_post_request_work_activity_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdIncidentsWorkActivitiesPostRequestWorkActivity from a dict
rest_v10_companies_company_id_incidents_work_activities_post_request_work_activity_from_dict = RestV10CompaniesCompanyIdIncidentsWorkActivitiesPostRequestWorkActivity.from_dict(rest_v10_companies_company_id_incidents_work_activities_post_request_work_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


