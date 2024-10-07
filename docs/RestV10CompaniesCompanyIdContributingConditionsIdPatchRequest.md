# RestV10CompaniesCompanyIdContributingConditionsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contributing_condition** | [**RestV10CompaniesCompanyIdContributingConditionsIdPatchRequestContributingCondition**](RestV10CompaniesCompanyIdContributingConditionsIdPatchRequestContributingCondition.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_contributing_conditions_id_patch_request import RestV10CompaniesCompanyIdContributingConditionsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdContributingConditionsIdPatchRequest from a JSON string
rest_v10_companies_company_id_contributing_conditions_id_patch_request_instance = RestV10CompaniesCompanyIdContributingConditionsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdContributingConditionsIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_contributing_conditions_id_patch_request_dict = rest_v10_companies_company_id_contributing_conditions_id_patch_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdContributingConditionsIdPatchRequest from a dict
rest_v10_companies_company_id_contributing_conditions_id_patch_request_from_dict = RestV10CompaniesCompanyIdContributingConditionsIdPatchRequest.from_dict(rest_v10_companies_company_id_contributing_conditions_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


