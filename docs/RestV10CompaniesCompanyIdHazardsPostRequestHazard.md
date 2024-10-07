# RestV10CompaniesCompanyIdHazardsPostRequestHazard

Hazard object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Hazard | 
**active** | **bool** | Flag that denotes if the Hazard is available for use | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_hazards_post_request_hazard import RestV10CompaniesCompanyIdHazardsPostRequestHazard

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdHazardsPostRequestHazard from a JSON string
rest_v10_companies_company_id_hazards_post_request_hazard_instance = RestV10CompaniesCompanyIdHazardsPostRequestHazard.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdHazardsPostRequestHazard.to_json())

# convert the object into a dict
rest_v10_companies_company_id_hazards_post_request_hazard_dict = rest_v10_companies_company_id_hazards_post_request_hazard_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdHazardsPostRequestHazard from a dict
rest_v10_companies_company_id_hazards_post_request_hazard_from_dict = RestV10CompaniesCompanyIdHazardsPostRequestHazard.from_dict(rest_v10_companies_company_id_hazards_post_request_hazard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


