# RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**about** | **str** | About | [optional] 
**approval_state** | **str** | Approval state | [optional] 
**built_by** | **str** | Built by | [optional] 
**costs_money** | **bool** | Costs money | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**description** | **str** | Description | [optional] 
**feature_bullets** | **List[str]** | Feature bullets | [optional] 
**helpful_links** | [**List[RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceAppHelpfulLinksInner]**](RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceAppHelpfulLinksInner.md) | Helpful links | [optional] 
**how_it_works** | **str** | How it works | [optional] 
**live** | **bool** | Live | [optional] 
**pictures** | [**List[RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceAppPicturesInner]**](RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceAppPicturesInner.md) | Pictures | [optional] 
**public_name** | **str** | Public name | [optional] 
**requirements** | **List[str]** | Requirements | [optional] 
**small_logo_url** | **str** | URL to the small logo image | [optional] 
**state** | **str** | State | [optional] 
**support_email** | **str** | Support email | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**version** | **int** | Version | [optional] 
**videos** | [**List[RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceAppVideosInner]**](RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceAppVideosInner.md) | Videos | [optional] 
**website_link** | [**RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceAppWebsiteLink**](RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceAppWebsiteLink.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_app_installations_get200_response_inner_all_of_developer_app_marketplace_app import RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp from a JSON string
rest_v10_app_installations_get200_response_inner_all_of_developer_app_marketplace_app_instance = RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp.from_json(json)
# print the JSON string representation of the object
print(RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp.to_json())

# convert the object into a dict
rest_v10_app_installations_get200_response_inner_all_of_developer_app_marketplace_app_dict = rest_v10_app_installations_get200_response_inner_all_of_developer_app_marketplace_app_instance.to_dict()
# create an instance of RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp from a dict
rest_v10_app_installations_get200_response_inner_all_of_developer_app_marketplace_app_from_dict = RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp.from_dict(rest_v10_app_installations_get200_response_inner_all_of_developer_app_marketplace_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


