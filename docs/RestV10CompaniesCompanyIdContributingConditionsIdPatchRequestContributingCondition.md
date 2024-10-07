# RestV10CompaniesCompanyIdContributingConditionsIdPatchRequestContributingCondition

ContributingCondition object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Contributing Condition | [optional] 
**active** | **bool** | Flag that denotes if the Contributing Condition is available for use | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_contributing_conditions_id_patch_request_contributing_condition import RestV10CompaniesCompanyIdContributingConditionsIdPatchRequestContributingCondition

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdContributingConditionsIdPatchRequestContributingCondition from a JSON string
rest_v10_companies_company_id_contributing_conditions_id_patch_request_contributing_condition_instance = RestV10CompaniesCompanyIdContributingConditionsIdPatchRequestContributingCondition.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdContributingConditionsIdPatchRequestContributingCondition.to_json())

# convert the object into a dict
rest_v10_companies_company_id_contributing_conditions_id_patch_request_contributing_condition_dict = rest_v10_companies_company_id_contributing_conditions_id_patch_request_contributing_condition_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdContributingConditionsIdPatchRequestContributingCondition from a dict
rest_v10_companies_company_id_contributing_conditions_id_patch_request_contributing_condition_from_dict = RestV10CompaniesCompanyIdContributingConditionsIdPatchRequestContributingCondition.from_dict(rest_v10_companies_company_id_contributing_conditions_id_patch_request_contributing_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


