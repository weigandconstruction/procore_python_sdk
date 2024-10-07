# RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequestHarmSource

Harm Source object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Harm Source | 
**active** | **bool** | Flag that denotes if the Harm Source is available for use | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_incidents_harm_sources_post_request_harm_source import RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequestHarmSource

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequestHarmSource from a JSON string
rest_v10_companies_company_id_incidents_harm_sources_post_request_harm_source_instance = RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequestHarmSource.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequestHarmSource.to_json())

# convert the object into a dict
rest_v10_companies_company_id_incidents_harm_sources_post_request_harm_source_dict = rest_v10_companies_company_id_incidents_harm_sources_post_request_harm_source_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequestHarmSource from a dict
rest_v10_companies_company_id_incidents_harm_sources_post_request_harm_source_from_dict = RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequestHarmSource.from_dict(rest_v10_companies_company_id_incidents_harm_sources_post_request_harm_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


