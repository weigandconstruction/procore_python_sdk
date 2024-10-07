# RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard

Hazard object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Hazard | [optional] 
**active** | **bool** | Flag that denotes if the Hazard is available for use | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_hazards_id_patch_request_hazard import RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard from a JSON string
rest_v10_companies_company_id_hazards_id_patch_request_hazard_instance = RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard.to_json())

# convert the object into a dict
rest_v10_companies_company_id_hazards_id_patch_request_hazard_dict = rest_v10_companies_company_id_hazards_id_patch_request_hazard_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard from a dict
rest_v10_companies_company_id_hazards_id_patch_request_hazard_from_dict = RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard.from_dict(rest_v10_companies_company_id_hazards_id_patch_request_hazard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


