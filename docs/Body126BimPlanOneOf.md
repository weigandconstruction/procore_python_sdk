# Body126BimPlanOneOf

BIM Plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_level_id** | **int** | ID of the BIM Level to be associated to the plan | 
**sheet_map_start** | [**Body125BimPlanOneOfSheetMapStart**](Body125BimPlanOneOfSheetMapStart.md) |  | [optional] 
**sheet_map_end** | [**Body125BimPlanOneOfSheetMapStart**](Body125BimPlanOneOfSheetMapStart.md) |  | [optional] 
**model_map_start** | [**Body125BimPlanOneOfModelMapStart**](Body125BimPlanOneOfModelMapStart.md) |  | [optional] 
**model_map_end** | [**Body125BimPlanOneOfModelMapStart**](Body125BimPlanOneOfModelMapStart.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body126_bim_plan_one_of import Body126BimPlanOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of Body126BimPlanOneOf from a JSON string
body126_bim_plan_one_of_instance = Body126BimPlanOneOf.from_json(json)
# print the JSON string representation of the object
print(Body126BimPlanOneOf.to_json())

# convert the object into a dict
body126_bim_plan_one_of_dict = body126_bim_plan_one_of_instance.to_dict()
# create an instance of Body126BimPlanOneOf from a dict
body126_bim_plan_one_of_from_dict = Body126BimPlanOneOf.from_dict(body126_bim_plan_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


