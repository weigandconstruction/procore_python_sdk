# RestV10BimModelsGet200ResponseInnerOneOf

BIM Model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**title** | **str** | BIM Model title. | [optional] 
**auto_publish** | **bool** | Model auto publishing setting. When set to true, a new model revision is automatically published when a new version of the input model file is uploaded | [optional] 
**project_id** | **int** | Unique identifier for the project. | [optional] 
**revisions_count** | **float** | No. of model revisions published | [optional] 
**web_url** | **str** | Deep link to Procore&#39;s Models Web Viewer. | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 
**current_revision_id** | **int** | Current Revision ID | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_models_get200_response_inner_one_of import RestV10BimModelsGet200ResponseInnerOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimModelsGet200ResponseInnerOneOf from a JSON string
rest_v10_bim_models_get200_response_inner_one_of_instance = RestV10BimModelsGet200ResponseInnerOneOf.from_json(json)
# print the JSON string representation of the object
print(RestV10BimModelsGet200ResponseInnerOneOf.to_json())

# convert the object into a dict
rest_v10_bim_models_get200_response_inner_one_of_dict = rest_v10_bim_models_get200_response_inner_one_of_instance.to_dict()
# create an instance of RestV10BimModelsGet200ResponseInnerOneOf from a dict
rest_v10_bim_models_get200_response_inner_one_of_from_dict = RestV10BimModelsGet200ResponseInnerOneOf.from_dict(rest_v10_bim_models_get200_response_inner_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


