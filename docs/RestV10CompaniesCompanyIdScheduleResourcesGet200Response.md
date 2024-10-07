# RestV10CompaniesCompanyIdScheduleResourcesGet200Response

Schedule Resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[RestV10CompaniesCompanyIdScheduleResourcesGet200ResponseResourcesInner]**](RestV10CompaniesCompanyIdScheduleResourcesGet200ResponseResourcesInner.md) | Resources | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_schedule_resources_get200_response import RestV10CompaniesCompanyIdScheduleResourcesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdScheduleResourcesGet200Response from a JSON string
rest_v10_companies_company_id_schedule_resources_get200_response_instance = RestV10CompaniesCompanyIdScheduleResourcesGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdScheduleResourcesGet200Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_schedule_resources_get200_response_dict = rest_v10_companies_company_id_schedule_resources_get200_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdScheduleResourcesGet200Response from a dict
rest_v10_companies_company_id_schedule_resources_get200_response_from_dict = RestV10CompaniesCompanyIdScheduleResourcesGet200Response.from_dict(rest_v10_companies_company_id_schedule_resources_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


