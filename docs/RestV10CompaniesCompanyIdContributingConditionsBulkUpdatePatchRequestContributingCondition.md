# RestV10CompaniesCompanyIdContributingConditionsBulkUpdatePatchRequestContributingCondition

IDs of all Contributing Conditions specified for bulk update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**active** | **bool** | Flag that denotes if the Contributing Conditions are available for use | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_contributing_conditions_bulk_update_patch_request_contributing_condition import RestV10CompaniesCompanyIdContributingConditionsBulkUpdatePatchRequestContributingCondition

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdContributingConditionsBulkUpdatePatchRequestContributingCondition from a JSON string
rest_v10_companies_company_id_contributing_conditions_bulk_update_patch_request_contributing_condition_instance = RestV10CompaniesCompanyIdContributingConditionsBulkUpdatePatchRequestContributingCondition.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdContributingConditionsBulkUpdatePatchRequestContributingCondition.to_json())

# convert the object into a dict
rest_v10_companies_company_id_contributing_conditions_bulk_update_patch_request_contributing_condition_dict = rest_v10_companies_company_id_contributing_conditions_bulk_update_patch_request_contributing_condition_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdContributingConditionsBulkUpdatePatchRequestContributingCondition from a dict
rest_v10_companies_company_id_contributing_conditions_bulk_update_patch_request_contributing_condition_from_dict = RestV10CompaniesCompanyIdContributingConditionsBulkUpdatePatchRequestContributingCondition.from_dict(rest_v10_companies_company_id_contributing_conditions_bulk_update_patch_request_contributing_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


