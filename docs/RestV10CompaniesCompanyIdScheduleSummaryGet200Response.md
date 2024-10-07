# RestV10CompaniesCompanyIdScheduleSummaryGet200Response

Company Schedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInner]**](RestV10CompaniesCompanyIdScheduleSummaryGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_schedule_summary_get200_response import RestV10CompaniesCompanyIdScheduleSummaryGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdScheduleSummaryGet200Response from a JSON string
rest_v10_companies_company_id_schedule_summary_get200_response_instance = RestV10CompaniesCompanyIdScheduleSummaryGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdScheduleSummaryGet200Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_schedule_summary_get200_response_dict = rest_v10_companies_company_id_schedule_summary_get200_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdScheduleSummaryGet200Response from a dict
rest_v10_companies_company_id_schedule_summary_get200_response_from_dict = RestV10CompaniesCompanyIdScheduleSummaryGet200Response.from_dict(rest_v10_companies_company_id_schedule_summary_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


