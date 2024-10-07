# RestV10CompaniesCompanyIdContributingBehaviorsBulkUpdatePatchRequestContributingBehavior

IDs of all Contributing Behaviors specified for bulk update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**active** | **bool** | Flag that denotes if the Contributing Behaviors are available for use | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch_request_contributing_behavior import RestV10CompaniesCompanyIdContributingBehaviorsBulkUpdatePatchRequestContributingBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdContributingBehaviorsBulkUpdatePatchRequestContributingBehavior from a JSON string
rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch_request_contributing_behavior_instance = RestV10CompaniesCompanyIdContributingBehaviorsBulkUpdatePatchRequestContributingBehavior.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdContributingBehaviorsBulkUpdatePatchRequestContributingBehavior.to_json())

# convert the object into a dict
rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch_request_contributing_behavior_dict = rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch_request_contributing_behavior_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdContributingBehaviorsBulkUpdatePatchRequestContributingBehavior from a dict
rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch_request_contributing_behavior_from_dict = RestV10CompaniesCompanyIdContributingBehaviorsBulkUpdatePatchRequestContributingBehavior.from_dict(rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch_request_contributing_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


